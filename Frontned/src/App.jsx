import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// import DetailsForm from "./detials-form"
import Orc from "./orc-test"

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
