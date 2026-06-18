import React from 'react';
import './Dashboard.css';

const Dashboard = () => {
  const userEmail = localStorage.getItem('user_email');

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_email');
    window.location.href = '/';
  };

  return (
    <div className="dashboard-container">
      <nav className="dashboard-nav">
        <div className="nav-brand">
          <div className="nav-logo">AC</div>
          <span>AuthCore</span>
        </div>
        <button onClick={handleLogout} className="logout-btn">
          Sign Out
        </button>
      </nav>

      <main className="dashboard-main">
        <div className="dashboard-header">
          <h1>Welcome to AuthCore</h1>
          <p>You've successfully authenticated to our system</p>
        </div>

        <div className="dashboard-grid">
          <div className="dashboard-card">
            <div className="card-icon">👤</div>
            <h3>Account</h3>
            <p className="card-email">{userEmail}</p>
            <button className="card-btn">Manage Account</button>
          </div>

          <div className="dashboard-card">
            <div className="card-icon">🔒</div>
            <h3>Security</h3>
            <p>Keep your account safe and secure</p>
            <button className="card-btn">Change Password</button>
          </div>

          <div className="dashboard-card">
            <div className="card-icon">⚙️</div>
            <h3>Settings</h3>
            <p>Customize your experience</p>
            <button className="card-btn">Preferences</button>
          </div>

          <div className="dashboard-card">
            <div className="card-icon">📚</div>
            <h3>Documentation</h3>
            <p>Learn about our platform</p>
            <button className="card-btn">View Docs</button>
          </div>
        </div>

        <div className="dashboard-footer">
          <div className="footer-content">
            <h3>Session Information</h3>
            <div className="session-info">
              <div className="info-item">
                <span className="label">User Email:</span>
                <span className="value">{userEmail}</span>
              </div>
              <div className="info-item">
                <span className="label">Login Time:</span>
                <span className="value">{new Date().toLocaleString()}</span>
              </div>
              <div className="info-item">
                <span className="label">Status:</span>
                <span className="value status-active">Active</span>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
