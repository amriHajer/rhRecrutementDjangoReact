import React, { useEffect, useState } from 'react';

const ListeEmployes = () => {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/employes/')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log("Fetched employees:", data); // Log des employés récupérés
        setEmployees(data);
      })
      .catch((error) => console.error('Error fetching employees:', error));
  }, []);

  const handleEdit = (employeeId) => {
    console.log("Edit employee with ID:", employeeId);
    // Logique pour éditer un employé (à compléter selon les besoins)
  };

  const handleDelete = (employeeId) => {
    console.log("Attempting to delete employee with ID:", employeeId);
    if (employeeId === undefined) {
      console.error('Employee ID is undefined');
      return;
    }
    
    if (window.confirm("Are you sure you want to delete this employee?")) {
      const url = `http://localhost:8000/api/employes/${employeeId}/`;
      console.log('Deleting employee at URL:', url); // Log de l'URL
      fetch(url, { method: 'DELETE' })
        .then((response) => {
          if (!response.ok) {
            return response.text().then(text => { throw new Error(`Error: ${text}`); });
          }
          // Mettre à jour la liste des employés après suppression
          setEmployees((prevEmployees) =>
            prevEmployees.filter((emp) => emp.user.id !== employeeId) // Modification ici pour utiliser emp.user.id
          );
          console.log("Employee deleted successfully.");
        })
        .catch((error) => console.error('Error deleting employee:', error));
    }
  };
  
  return (
    <div className="mx-auto max-w-270">
      <div className="grid grid-cols-5 gap-12">
        <div className="col-span-5 xl:col-span-12">
          <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
            <div className="border-b border-stroke py-4 px-7 dark:border-strokedark">
              <h3 className="font-medium text-black dark:text-white">Liste des Employés</h3>
            </div>
            <div className="p-7">
              <div className="max-w-full overflow-x-auto table-wrapper">
                <table className="table w-full border-collapse">
                  <thead>
                    <tr className="bg-gray-200 text-left">
                      {/* <th className="py-4 px-4 font-medium text-black">ID</th> Colonne ID ajoutée */}
                      <th className="py-4 px-4 font-medium text-black">Image</th>
                      <th className="py-4 px-4 font-medium text-black">Nom</th>
                      <th className="py-4 px-4 font-medium text-black">Position</th>
                      <th className="py-4 px-4 font-medium text-black">Département</th>
                      <th className="py-4 px-4 font-medium text-black">Téléphone</th>
                      <th className="py-4 px-4 font-medium text-black">Email</th>
                      <th className="py-4 px-4 font-medium text-black">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {employees.map((employee) => (
                      <tr key={employee.user.id} className="hover:bg-gray-50"> {/* Changement ici */}
                        {/* <td className="border-b py-4 px-4">{employee.user.id}</td> Accéder à l'ID ici */}
                        <td className="border-b py-4 px-4">
                          <img
                            src={employee.user.profile_picture ? `http://localhost:8000${employee.user.profile_picture}` : 'default_profile_picture.jpg'} // chemin par défaut si pas d'image
                            alt={`${employee.user.username}'s profile`}
                            className="w-12 h-12 rounded-full" // styliser l'image
                          />
                        </td>
                        <td className="border-b py-4 px-4">{employee.user.username}</td>
                        <td className="border-b py-4 px-4">{employee.position}</td>
                        <td className="border-b py-4 px-4">{employee.department}</td>
                        <td className="border-b py-4 px-4">{employee.tel || 'N/A'}</td>
                        <td className="border-b py-4 px-4">{employee.user.email}</td>
                        <td className="border-b py-4 px-4">
                          <button
                            onClick={() => handleEdit(employee.user.id)} // Utiliser employee.user.id ici
                            className="text-blue-500 hover:text-blue-700 mr-2"
                          >
                            Éditer
                          </button>
                          <button
                            onClick={() => handleDelete(employee.user.id)} // Utiliser employee.user.id ici
                            className="text-red-500 hover:text-red-700"
                          >
                            Supprimer
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ListeEmployes;
