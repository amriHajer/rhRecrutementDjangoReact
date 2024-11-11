import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css'; // Si vous avez un fichier CSS personnalisé
import Navbar from './Navbar';
import JobListing from './JobListing';

function Index() {
  return (
    <div className="index">
      <Navbar />
      <div className="container-fluid p-0">
        <div className="position-relative">
          <img
            className="img-fluid w-100"
            src="/src/pages/Acceuil/img/carousel-1.jpg"
            alt="Carousel 1"
            style={{ height: '80vh', objectFit: 'cover' }}
          />
          <div
            className="position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center"
            style={{ background: 'rgba(43, 57, 64, 0.5)' }}
          >
            <div className="container">
              <div className="row justify-content-start">
                <div className="col-10 col-lg-8">
                  <h1 className="display-3 text-white animated slideInDown mb-4">
                  Your Gateway to the Best Tech Jobs
                  </h1>
                  
                 
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="my-5"></div>

      {/* Section Job Listing */}
      <JobListing />
    </div>
  );
}

export default Index;
