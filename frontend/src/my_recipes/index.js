import React, { useState, useEffect } from 'react';
import Card from 'react-bootstrap/Card';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import axios from 'axios';
import './style.css';

function RecipePage() {
    const [recipes, setRecipes] = useState([]);
    const token = sessionStorage.getItem("token");
    const config = {
        headers: {
            "Authorization": "Bearer " + sessionStorage.getItem("token"),
        },
    };
    
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/accounts/my-recipes/', config)
            .then(response => setRecipes(response.data["Recipes created"]))
            .catch(error => console.log(error));
    }, []);

    // console.log('recipes:', recipes);

    return (
        <div className="container">
            <h3 className="display-5 mb-1 text-center" style={{ marginTop: '75px' }}>My Recipes</h3>

            <div className="row mt-5">
                {Array.isArray(recipes) && recipes.map(recipe => (
                    <div className="col-lg-4 col-md-4 col-6" key={recipe.id}>
                        <div className="card">
                            <div className="card-body">
                                <h5 className="card-title">{recipe.title}</h5>
                                <p className="card-text">{recipe.description}</p>
                                <a href={`/recipes/${recipe.id}`} className="btn btn-primary">View Recipe</a> {/* change this */}
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default RecipePage;