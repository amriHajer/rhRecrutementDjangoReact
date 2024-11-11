import React, { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMapMarkerAlt, faClock, faMoneyBillAlt, faCalendarAlt } from '@fortawesome/free-solid-svg-icons';

function JobListing() {
  const [jobOffers, setJobOffers] = useState([]); // État pour stocker les offres
  const [loading, setLoading] = useState(true); // État pour gérer le chargement

  useEffect(() => {
    // Fonction pour récupérer les données depuis l'API
    const fetchJobOffers = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/recrutement/offres');
        const data = await response.json();
        setJobOffers(data); // Mise à jour de l'état avec les données récupérées
        setLoading(false); // Fin du chargement
      } catch (error) {
        console.error("Error fetching job offers:", error);
        setLoading(false); // Fin du chargement en cas d'erreur
      }
    };

    fetchJobOffers(); // Appeler la fonction pour récupérer les données
  }, []); // Le tableau vide signifie que cette fonction sera appelée une seule fois, après le premier rendu.

  if (loading) {
    return <div>Loading...</div>; // Afficher un message de chargement pendant que les données sont récupérées
  }

  return (
    <div className="job-listing">
      {jobOffers.map((offer, index) => (
        <div className="job-item p-4 mb-4" key={index}>
          <div className="row g-4">
            <div className="col-sm-12 col-md-8 d-flex align-items-center">
              <img
                className="flex-shrink-0 img-fluid border rounded"
                src="/src/pages/Acceuil/img/lg.png"
                alt="Company Logo"
                style={{ width: '80px', height: '80px' }}
              />
              <div className="text-start ps-4">
                <h5 className="mb-3">{offer.titre}</h5>
                <span className="text-truncate me-3">
                  <FontAwesomeIcon icon={faMapMarkerAlt} className="text-success me-2" />
                  {offer.localisation}
                </span>
                <span className="text-truncate me-3">
                  <FontAwesomeIcon icon={faClock} className="text-success me-2" />
                  {offer.type_emploi || 'Full Time'}
                </span>
                <span className="text-truncate me-0">
                  <FontAwesomeIcon icon={faMoneyBillAlt} className="text-success me-2" />
                  {offer.salaire || '$0 - $0'}
                </span>
              </div>
            </div>
            <div className="col-sm-12 col-md-4 d-flex flex-column align-items-start align-items-md-end justify-content-center">
              <div className="d-flex mb-3">
                <a className="btn btn-success" href="#">
                  Apply Now
                </a>
              </div>
              <small className="text-truncate">
                <FontAwesomeIcon icon={faCalendarAlt} className="text-success me-2" />
                Date Line: {new Date(offer.date_expiration).toLocaleDateString()}
              </small>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default JobListing;
