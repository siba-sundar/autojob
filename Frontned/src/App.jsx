import { useState } from 'react'
import ReactDOM from "react-dom/client";

// imported components
import Home from "./pages/Home.jsx"
import LinkedinHome from "./components/linkedin/Linkedin.jsx";
import IntershalaHome from  "./components/intershala/Intershala.jsx"
import NavBar from "./components/NavBar.jsx"

import {createBrowserRouter, RouterProvider} from  "react-router-dom"



function App() {

  const router = createBrowserRouter([
    {
      path:"/",
      element:<><NavBar/><Home/></>
    },
    {
      path:"/linkedin",
      element:<><NavBar/><LinkedinHome/></>
    },
    {
      path:"/intershala",
      element:<><NavBar/><IntershalaHome/></>
    }
  ])

  const [count, setCount] = useState(0)

  return (
    <>
    <div>
      Hhahahah
    </div>
    
    <RouterProvider router={router}/>
    </>
  )
}

export default App
