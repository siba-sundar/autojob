import { useState } from 'react'
import ReactDOM from "react-dom/client";
import {createBrowserRouter} from "react-router-dom"
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'



function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <DetailsForm/> */}
    <Orc/>
    </>
  )
}

export default App
