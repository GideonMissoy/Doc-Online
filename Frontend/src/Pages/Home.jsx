import React from 'react';
import Navbar from '../Components/Nav';

function Home() {
  return (
    <div>
      <div>
        <Navbar />
        <div className='flex justify-center align-center text-center'>
          <h2 className='font-black text-bold'>
            Connecting Patients with the Right Doctors
          </h2>
          <p>
            Search for symptoms, find specialized doctors, and book sessions
            easily. Your health journey starts here.
          </p>
          <Link
            to='/register'
            className='bg-green-600 text-white py-2 px-3 lg:px-5 font-bold rounded-full'
          >
            Get Started
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Home;
