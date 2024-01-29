import React from 'react';
import './Header.css';


function Header() {
  return (
    <header>
      <div className="container">
        <div className="logo">
          <img src="/MovieLogo.jpg" alt="Cinema E-Booking" />
        </div>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/movies">Movies</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/about">Login</a></li>
            {/* Add more navigation links as needed */}
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
