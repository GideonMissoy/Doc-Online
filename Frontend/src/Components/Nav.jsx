import React from 'react';

function Navbar() {
  return (
    <div>
      <div className='flex flex-row justify-between py-3 px-2 bg-slate-950 text-white'>
        <div className='lg:ml-11 px-2 lg:px-5 py-2'>
          <a href='/'>Jenga</a>
        </div>
        <div>
          <ul className='flex flex-row'>
            <li className='px-2 lg:px-5 py-2 hover:bg-slate-800 rounded-full mr-2'>
              <Link to='/'>About</Link>
            </li>
            <li className='px-2 lg:px-5 py-2 hover:bg-slate-800 rounded-full mr-2'>
              <Link to='/'>Features</Link>
            </li>
            <li className='px-2 lg:px-5 py-2 hover:bg-slate-800 rounded-full mr-2'>
              <Link to='/'>How it works</Link>
            </li>
            <li className='px-2 lg:px-5 py-2 hover:bg-slate-800 rounded-full mr-2'>
              <Link to='/'>Contact</Link>
            </li>
          </ul>
        </div>
        <div className='lg:mr-11 px-2 py-2 lg:px-5 rounded-full bg-green-700 hover:bg-green-500 text-black'>
          <Link to='/login'>Login</Link>
        </div>
      </div>
    </div>
  );
}

export default Navbar;
