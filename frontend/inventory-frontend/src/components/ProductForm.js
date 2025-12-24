import React, { useState, useEffect } from 'react';
import api from '../api/axios';
import './ProductForm.css';

const ProductForm = ({ product, onSuccess, onCancel }) => {
  const [formData, setFormData] = useState({
    name: '',
    price: '',
    stock: '',
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (product) {
      setFormData({
        name: product.name,
        price: product.price,
        stock: product.stock,
      });
    }
  }, [product]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      if (product) {
        await api.put(`/products/${product.id}/`, formData);
      } else {
        await api.post('/products/', formData);
      }
      onSuccess();
    } catch (err) {
      const errorMsg = err.response?.data;
      if (typeof errorMsg === 'object') {
        const errors = Object.entries(errorMsg)
          .map(([key, value]) => `${key}: ${value}`)
          .join(', ');
        setError(errors);
      } else {
        setError('Failed to save product');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="product-form-overlay">
      <div className="product-form-card">
        <h3>{product ? 'Edit Product' : 'Add New Product'}</h3>

        <form onSubmit={handleSubmit}>
          {error && <div className="error-message">{error}</div>}

          <div className="form-group">
            <label htmlFor="name">Product Name *</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="price">Price (₹) *</label>
            <input
              type="number"
              id="price"
              name="price"
              value={formData.price}
              onChange={handleChange}
              min="0"
              step="0.01"
              required
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label htmlFor="stock">Stock *</label>
            <input
              type="number"
              id="stock"
              name="stock"
              value={formData.stock}
              onChange={handleChange}
              min="0"
              required
              disabled={loading}
            />
          </div>

          <div className="form-actions">
            <button
              type="button"
              className="btn btn-secondary"
              onClick={onCancel}
              disabled={loading}
            >
              Cancel
            </button>
            <button
              type="submit"
              className="btn btn-primary"
              disabled={loading}
            >
              {loading ? 'Saving...' : 'Save'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ProductForm;
