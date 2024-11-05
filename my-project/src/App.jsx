import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Components/Login";
import Home from "./Components/Home";

function App() {
  return (
    <Router>
      <main>
        <Routes>
          {/* Rota para a tela de login */}
          <Route path="/" element={<Login />} />
          {/* Rota para a tela home */}
          <Route path="/home" element={<Home />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
