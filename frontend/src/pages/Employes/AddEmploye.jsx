import React, { useState } from 'react';
import AxiosInstance from './AxiosInstance'; // Ensure AxiosInstance is properly set up

const Employe = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    tel: '', // Ajout du champ pour le numéro de téléphone
    password: '',
    password2: '',
    position: '',
    department: '',
    profile_picture: null,
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

  const handleFileChange = (e) => {
    setFormData({
      ...formData,
      profile_picture: e.target.files[0],
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null); // Reset error on each submission

    if (formData.password !== formData.password2) {
      setError("Passwords do not match.");
      return;
    }

    const signupData = new FormData();
    Object.keys(formData).forEach((key) => {
      signupData.append(key, formData[key]);
    });

    try {
      const response = await AxiosInstance.post('/api/signup/employe/', signupData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setSuccess("Registration successful!");
      setError(null);
      console.log("Server response:", response.data);
    } catch (err) {
      setError(err.response?.data?.error || "An error occurred during registration.");
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
                <center><strong>Ajouter un employé</strong></center>
              </h3>
            </div>
            <div className="p-7">
              <form onSubmit={handleSubmit}>
                <div className="mb-5.5 flex flex-col gap-5.5 sm:flex-row">
                  <div className="w-full sm:w-1/2">
                    <input
                      className="w-full rounded border border-stroke bg-gray py-3 pl-11.5 pr-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                      type="text"
                      name="username"
                      placeholder="Enter your full name"
                      onChange={handleChange}
                      value={formData.username}
                      required
                    />
                  </div>
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 pl-11.5 pr-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="email"
                    name="email"
                    placeholder="Enter your email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                  />
                </div>

                {/* Champ pour le numéro de téléphone */}
                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 pl-11.5 pr-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="tel"
                    name="tel"
                    placeholder="nombre tel "
                    value={formData.tel}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="text"
                    name="department"
                    placeholder="Department"
                    value={formData.department}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="text"
                    name="position"
                    placeholder="Position"
                    value={formData.position}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={formData.password}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    className="w-full rounded border border-stroke bg-gray py-3 px-4.5 text-black focus:border-primary focus-visible:outline-none dark:border-strokedark dark:bg-meta-4 dark:text-white dark:focus:border-primary"
                    type="password"
                    name="password2"
                    placeholder="Re-enter Password"
                    value={formData.password2}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="mb-5.5">
                  <input
                    type="file"
                    className="w-full cursor-pointer rounded-lg border-[1.5px] border-stroke bg-transparent outline-none transition file:mr-5 file:border-collapse file:cursor-pointer file:border-0 file:border-r file:border-solid file:border-stroke file:bg-whiter file:py-3 file:px-5 file:hover:bg-primary file:hover:bg-opacity-10 focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:file:border-form-strokedark dark:file:bg-white/30 dark:file:text-white dark:focus:border-primary"
                    onChange={handleFileChange}
                    accept="image/*"
                  />
                </div>

                {error && <p className="text-red-500">{error}</p>}
                {success && <p className="text-green-500">{success}</p>}

                <button
                  type="submit"
                  className="inline-flex items-center justify-center rounded bg-primary py-2 px-4 text-center font-medium text-white hover:bg-opacity-90 lg:px-4 xl:px-6"
                >
                  Register Employee
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Employe;
