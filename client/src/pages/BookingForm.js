import React, { useState, useEffect } from 'react';
import { useFormik } from 'formik';
import * as yup from 'yup';

function BookingForm() {
    const [pets, setPets] = useState([]);
    const [sitters, setSitters] = useState([]);

    // Load dropdown data on component mount
    useEffect(() => {
        fetch('http://localhost:5555/pets').then(r => r.json()).then(setPets);
        fetch('http://localhost:5555/users').then(r => r.json()).then(setSitters);
    }, []);