import React from 'react';
import Navbar from '../Components/Nav';
import { Link } from 'react-router-dom';
import Aboutpic from '../assets/about-image.jpg';

function Home() {
  return (
    <div>
      <div className='lg:py-4 '>
        <Navbar />
        <div className='flex flex-row lg:mx-11'>
          <div className='flex flex-col justify-center align-center text-center text-black lg:w-2/5'>
            <h2 className='text-3xl text-bold'>
              Connecting Patients with the Right Doctors
            </h2>
            <br />
            <p>
              Search for symptoms, find specialized doctors, and book sessions
              easily. Your health journey starts here.
            </p>
            <button className='justify-center bg-green-500 hover:bg-green-700 text-black rounded-full lg:px-6 px-5 py-2 my-5'>
              <Link to='/register'>Get Started</Link> 
            </button>
          </div>
          <div className='lg:w-3/5'>
            <img src={Aboutpic} alt='' />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
