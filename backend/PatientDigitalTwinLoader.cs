using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

[System.Serializable]
public class PatientData
{
    public string patient_id;
    public string age;
    public string sex;
    public string stage;
    public string egfr;
    public float efficiency;
    public float resistance;
}

public class PatientDigitalTwinLoader : MonoBehaviour
{
    [Header("API Settings")]
    [Tooltip("Copiez ici l'URL ngrok donnée par Colab")]
    public string apiBaseUrl = "https://votre-url.ngrok-free.app";

    [Header("Simulation Controllers")]
    public TumorSimulationController tumorController;
    public DrugParticleSystem drugSystem;

    private List<PatientData> allPatients = new List<PatientData>();
    private PatientData currentPatient;

    void Start()
    {
        if (apiBaseUrl.Contains("votre-url"))
        {
            Debug.LogError("❌ Veuillez entrer l'URL de l'API Unity (ngrok) dans l'inspecteur !");
            return;
        }
        StartCoroutine(LoadFirstPatient());
    }

    IEnumerator LoadFirstPatient()
    {
        // 1. Charger la liste des patients
        string listUrl = apiBaseUrl + "/api/patients";
        using (UnityWebRequest request = UnityWebRequest.Get(listUrl))
        {
            yield return request.SendWebRequest();
            if (request.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError("Erreur chargement liste patients : " + request.error);
                yield break;
            }

            // Parser le tableau JSON
            string jsonArray = request.downloadHandler.text;
            allPatients = ParseJsonArray<PatientData>(jsonArray);
            Debug.Log($"✅ {allPatients.Count} patients chargés depuis l'API");

            if (allPatients.Count > 0)
            {
                // 2. Charger le premier patient en détail (ou celui que vous voulez)
                StartCoroutine(LoadPatientDetails(allPatients[0].patient_id));
            }
        }
    }

    IEnumerator LoadPatientDetails(string patientId)
    {
        string url = apiBaseUrl + "/api/patient/" + patientId;
        using (UnityWebRequest request = UnityWebRequest.Get(url))
        {
            yield return request.SendWebRequest();
            if (request.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError($"Patient {patientId} introuvable");
                yield break;
            }

            currentPatient = JsonUtility.FromJson<PatientData>(request.downloadHandler.text);
            Debug.Log($"📋 Patient chargé : {currentPatient.patient_id} | Efficacité {currentPatient.efficiency * 100}% | Résistance {currentPatient.resistance * 100}%");

            // Appliquer les valeurs à la simulation
            if (tumorController != null)
            {
                tumorController.SetTreatmentEfficacy(currentPatient.efficiency);
                tumorController.SetResistanceRisk(currentPatient.resistance);
            }

            if (drugSystem != null)
            {
                drugSystem.SetEfficiency(currentPatient.efficiency);
            }
        }
    }

    // Helper pour parser un tableau JSON (car Unity ne le fait pas directement)
    private List<T> ParseJsonArray<T>(string json)
    {
        string wrapped = "{\"items\":" + json + "}";
        Wrapper<T> wrapper = JsonUtility.FromJson<Wrapper<T>>(wrapped);
        return wrapper.items;
    }

    [System.Serializable]
    private class Wrapper<T>
    {
        public List<T> items;
    }
}
