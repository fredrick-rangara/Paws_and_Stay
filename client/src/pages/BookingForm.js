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

    const schema = yup.object().shape({
        pet_id: yup.string().required("Please select a pet"),
        sitter_id: yup.string().required("Please select a sitter"),
        daily_rate: yup.number().required("Rate is required").positive(),
        special_instructions: yup.string().min(5, "Give the sitter more detail!")
    });

    const formik = useFormik({
        initialValues: { pet_id: '', sitter_id: '', daily_rate: '', special_instructions: '' },
        validationSchema: schema,
        onSubmit: (values) => {
            fetch('http://localhost:5555/stay_sessions', {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(values)
            })
            .then(res => {
                if (res.ok) alert("Booking Successful!");
            });
        }
    });