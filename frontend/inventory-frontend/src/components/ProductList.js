import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import api from '../api/axios';
import ProductForm from './ProductForm';
import './ProductList.css';

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [editingProduct, setEditingProduct] = useState(null);

  const { isAdmin } = useAuth();

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      setLoading(true);
      const response = await api.get('/products/');
      setProducts(response.data.results || response.data);
      setError('');
    } catch (err) {
      setError('Failed to load products');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this product?')) {
      return;
    }

    try {
      await api.delete(`/products/${id}/`);
      setProducts(products.filter(p => p.id !== id));
    } catch (err) {
      alert('Failed to delete product');
      console.error(err);
    }
  };

  const handleEdit = (product) => {
    setEditingProduct(product);
    setShowForm(true);
  };

  const handleFormSuccess = () => {
    setShowForm(false);
    setEditingProduct(null);
    fetchProducts();
  };

  const handleFormCancel = () => {
    setShowForm(false);
    setEditingProduct(null);
  };

  if (loading) {
    return <div className="loading">Loading products...</div>;
  }

  return (
    <div className="product-list-container">
      <div className="product-list-header">
        <h2>Products</h2>
        {isAdmin() && (
          <button
            className="btn btn-primary"
            onClick={() => setShowForm(true)}
          >
            Add Product
          </button>
        )}
      </div>

      {error && <div className="error-message">{error}</div>}

      {showForm && (
        <ProductForm
          product={editingProduct}
          onSuccess={handleFormSuccess}
          onCancel={handleFormCancel}
        />
      )}

      <div className="product-grid">
        {products.length === 0 ? (
          <p className="no-products">No products available</p>
        ) : (
          products.map((product) => (
            <div key={product.id} className="product-card">
              <h3>{product.name}</h3>
              <div className="product-details">
                <p className="product-price">₹{parseFloat(product.price).toFixed(2)}</p>
                <p className="product-stock">Stock: {product.stock}</p>
              </div>
              {isAdmin() && (
                <div className="product-actions">
                  <button
                    className="btn btn-secondary"
                    onClick={() => handleEdit(product)}
                  >
                    Edit
                  </button>
                  <button
                    className="btn btn-danger"
                    onClick={() => handleDelete(product.id)}
                  >
                    Delete
                  </button>
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default ProductList;
