import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';  // Import CSS Bootstrap
import 'bootstrap/dist/js/bootstrap.bundle.min.js'; // Import JS Bootstrap

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-white shadow sticky-top">
      <div className="container">
        {/* Logo */}
        <Link to="/" className="navbar-brand">
          <h1 className="m-0 text-success">Coding</h1>
        </Link>
        
        {/* Bouton hamburger pour mobile */}
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        {/* Menu */}
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            {/* Liens de navigation */}
            <li className="nav-item">
              <Link to="/register" className="nav-link">
                Signup
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/login" className="nav-link">
                Signin
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
