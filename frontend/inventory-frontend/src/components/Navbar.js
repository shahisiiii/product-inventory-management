import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Navbar.css';

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  if (!user) return null;

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-brand">
          <h1>Inventory System</h1>
        </div>

        <div className="navbar-user">
          <div className="user-info">
            <span className="user-email">{user.email}</span>
            <span className={`user-role ${user.role.toLowerCase()}`}>
              {user.role}
            </span>
          </div>
          <button className="btn btn-logout" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
