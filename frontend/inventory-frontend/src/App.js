import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Login from './components/Login';
import ProductList from './components/ProductList';
import Navbar from './components/Navbar';
import './App.css';

const PrivateRoute = ({ children }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return user ? children : <Navigate to="/login" />;
};

const AppRoutes = () => {
  const { user } = useAuth();

  return (
    <>
      <Navbar />
      <Routes>
        <Route
          path="/login"
          element={user ? <Navigate to="/products" /> : <Login />}
        />
        <Route
          path="/products"
          element={
            <PrivateRoute>
              <ProductList />
            </PrivateRoute>
          }
        />
        <Route path="/" element={<Navigate to="/products" />} />
      </Routes>
    </>
  );
};

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
