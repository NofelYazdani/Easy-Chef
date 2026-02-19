import './App.css';
// import Signup from './signup';
import Home from './home';
import Login from './login';
import MyRecipes from './my_recipes';
import React, { useEffect } from 'react';
import { useNavigate, BrowserRouter, Routes, Route } from 'react-router-dom';


function App() {
  // const token = sessionStorage.getItem("token");
  // const navigate = useNavigate();

  // useEffect(() => {
  //   if (token == null) {
  //     navigate("/login");
  //   }
  // }, [navigate, token]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MyRecipes />}> </Route>
        <Route path="/login" element={<Login />}></Route>
        <Route path="/home" element={<Home />}> </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
