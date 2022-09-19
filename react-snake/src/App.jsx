import React from 'react'
import { Routes, Route} from "react-router-dom";
import Snake from './Snake'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Snake />}></Route>
    </Routes>
  );
}

export default App;