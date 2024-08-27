import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import Home from './Pages/Home';
import Register from './Pages/Auth/Register';
import Login from './Pages/Auth/Login';
import ForgotPassword from './Pages/Auth/ForgotPassword';
import VerifyEmail from './Pages/Auth/VerifyEmail';

function Logout() {
  localStorage.clear();
  return <Navigate to='/' />;
}

function RegisterAndLogout() {
  localStorage.clear();
  return <Register />;
}

function App() {
  return (
    <div>
      <Router>
        <ToastContainer />
        <Routes>
          <Route index element={<Home />} />
          <Route exact path='/' element={<Home />} />
          <Route path='/login' element={<Login />} />
          <Route path='/logout' element={<Logout />} />
          <Route path='/register' element={<RegisterAndLogout />} />
          <Route path='/reset-password' element={<ForgotPassword />} />
          <Route path='/verify-email' element={<VerifyEmail />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
