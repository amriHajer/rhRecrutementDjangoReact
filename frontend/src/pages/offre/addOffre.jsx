import React, { useState } from 'react';
import AxiosInstance from './AxiosInstance'; // Ensure AxiosInstance is properly set up


const AddOffre = () => {
  const [formData, setFormData] = useState({
    titre: '',
    description: '',
    date_expiration: '',
    entreprise: '',
    salaire: '',
    localisation: '',
  });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Reset error on each submission

    try {
        const response = await AxiosInstance.post('/api/recrutement/offres/', formData);
      setSuccess("Offre ajoutée avec succès !");
      setError(null);
      console.log("Server response:", response.data);
    } catch (err) {
      setError(err.response?.data?.error || "Une erreur est survenue lors de l'ajout de l'offre.");
      setSuccess(null);
    }
  };

  return (
    <div className="mx-auto max-w-270">
      <div className="grid grid-cols-5 gap-8">
        <div className="col-span-5 xl:col-span-3">
          <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
            <div className="border-b border-stroke py-4 px-7 dark:border-strokedark">
              <h3 className="font-medium text-black dark:text-white">
                <center><strong>Ajouter une Offre</strong></center>
              </h3>
            </div>
            <div className="p-7">
              <form onSubmit={handleSubmit}>
                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="text"
                    name="titre"
                    placeholder="Titre de l'offre"
                    onChange={handleChange}
                    value={formData.titre}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <textarea
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    name="description"
                    placeholder="Description de l'offre"
                    onChange={handleChange}
                    value={formData.description}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="date"
                    name="date_expiration"
                    onChange={handleChange}
                    value={formData.date_expiration}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="text"
                    name="entreprise"
                    placeholder="Nom de l'entreprise"
                    onChange={handleChange}
                    value={formData.entreprise}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="number"
                    name="salaire"
                    placeholder="Salaire proposé"
                    onChange={handleChange}
                    value={formData.salaire}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="text"
                    name="localisation"
                    placeholder="Localisation"
                    onChange={handleChange}
                    value={formData.localisation}
                    required
                  />
                </div>

                {error && <p className="text-red-500">{error}</p>}
                {success && <p className="text-green-500">{success}</p>}

                <button
                  type="submit"
                  className="inline-flex items-center justify-center rounded bg-primary py-2 px-4 text-center font-medium text-white hover:bg-opacity-90 lg:px-4 xl:px-6"
                >
                  Ajouter l'Offre
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AddOffre;
