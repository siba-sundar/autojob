import React from 'react'
import {Link} from "react-router-dom"


const NavBar = () => {
    
    return (
        <>
        <ul>
            <li><Link to="/linkedin">Linkedin</Link></li>
            <li><Link to="/intershala">Intershala</Link></li>
            <li><Link to="/">Home</Link></li>
        </ul>
        </>
    )
}

export default NavBar