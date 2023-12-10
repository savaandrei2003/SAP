import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import './App.css';
import Home from './pages/Home/Home';
import Cauta from './pages/Cauta/Cauta';



function App() {
  return (
    <div >
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cauta" element={<Cauta />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
