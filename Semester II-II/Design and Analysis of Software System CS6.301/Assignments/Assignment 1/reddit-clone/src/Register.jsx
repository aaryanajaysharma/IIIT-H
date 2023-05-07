import React, { useState } from 'react';

export const Register = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('email', email);
        console.log('password', password);
    }
    return (
    <div className='auth-form-container'>
        <form className='register-form' onSubmit={handleSubmit}>
            <label htmlFor="name">Full name</label>
            <input value={name} onChange={(e)=> setName(e.target.value)} type="text" placeholder="Enter your full name here" id="name" name="name"/>
            <label htmlFor="email">Email</label>
            <input value={email} onChange={(e)=> setEmail(e.target.value)} type="email" placeholder="youremail@here.com" id="email" name="email"/>
            <label htmlFor="password">Password</label>
            <input value={password} onChange={(e)=> setPassword(e.target.value)} type="password" placeholder="Enter your password here" id="password" name="password"/>
            <button type="submit">Login</button>
        </form>
        <button className='link-btn' onClick={() => props.onFormSwitch('login')}>Already have an account? Login here.</button>
    </div> 
    );
};