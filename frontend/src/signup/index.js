import { useState } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUtensils } from '@fortawesome/free-solid-svg-icons';
import './style.css'
import axios from 'axios';
import { useNavigate} from 'react-router-dom';


function Signup() {
  const navigate = useNavigate();
  const [formErr, setFormErr] = useState({});
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = {
      first_name: firstName,
      last_name: lastName,
      email: email,
      phone: phone,
      password: password,
      password2: confirmPassword,
    };
    axios.post('http://127.0.0.1:8000/accounts/register/', formData)
      .then((response) => {
        console.log('Signup successful:', response.data);
        // Navigate to home page after signing up
        navigate('/home');
      })
      .catch((error) => {
        console.error('Signup failed:', error.response.data);
        // setFormError(error.response.data);
      });
  };

const validation = (formValue) => {
  const errors = {};
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;
  if (!formValue.username) {
    errors.username = "Username is required."
  }
  if (!formValue.password) {
    errors.password = "Password is required."
  }
  if (!formValue.password2) {
    errors.password2 = "Confirm Password is required."
  } else if (formValue.password != formValue.password2) {
    errors.password2 = "Password doesn't match."
  }
  if (!formValue.email) {
    errors.email = "Email is required."
  } else if (!emailRegex.test(formValue.email)) {
    errors.email = "Email Format Invalid."
  }
  if (!formValue.firstname) {
    errors.firstname = "Firstname is required."
  }
  if (!formValue.lastname) {
    errors.lastname = "Lastname is required."
  }
  return errors;
}

  return (
    <section className="vh-100">
      <Container fluid>
        <Row>
          <Col sm={6} className="px-0 d-none d-sm-block">
            <img
              src={require("./background02.jpg")}
              alt="Signup image"
              className="w-100 vh-100"
              style={{ objectFit: 'cover', objectPosition: 'right' }}
            />
          </Col>
          <Col sm={6} className="text-black">
            <div className="px-5 ms-xl-4">
              <FontAwesomeIcon icon={faUtensils} className="fa-2x me-3 pt-5" />
              <a
                className="h1 fw-bold border-0 bg-white"
                style={{ textDecoration: 'none', color: 'black' }}
                type="button"
                onClick={() => navigate("/home")}
              >
                Easy Chef
              </a>
            </div>

            <div className="d-flex align-items-center h-custom-2 px-5 ms-xl-4 mt-5 pt-5 pt-xl-0 mt-xl-n5">
              <Form onSubmit={handleSubmit} className="rounded bg-white shadow p-5">
                <h3 className="text-dark fw-bolder fs-4 mb-2">Create an Account</h3>
                <Form.Group className="form-floating mb-3" controlId="floatingPassword">
                  <Form.Control
                    type="text"
                    placeholder="First Name"
                    value={firstName}
                    onChange={(event) => setFirstName(event.target.value)}
                  />
                  <Form.Label>First Name</Form.Label>
                </Form.Group>
                <Form.Group className="form-floating mb-3" controlId="floatingPassword">
                  <Form.Control
                    type="text"
                    placeholder="Last Name"
                    value={lastName}
                    onChange={(event) => setLastName(event.target.value)}
                  />
                  <Form.Label>Last Name</Form.Label>
                </Form.Group>
                <Form.Group className="form-floating mb-3" controlId="floatingPassword">
                  <Form.Control
                    type="email"
                    placeholder="name@example.com"
                    value={email}
                    onChange={(event) => setEmail(event.target.value)}
                  />
                  <Form.Label>Email address</Form.Label>
                </Form.Group>
                <Form.Group className="form-floating mb-3" controlId="floatingPassword">
                  <Form.Control
                    type="tel"
                    placeholder="123-456-7890"
                    // pattern="[0-9]{3}[0-9]{3}[0-9]{4}"
                    value={phone}
                    onChange={(event) => setPhone(event.target.value)}
                  />
                  <Form.Label>Phone number</Form.Label>
                </Form.Group>
                <Form.Group className="form-floating mb-3" controlId="floatingPassword">
                  <Form.Control
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                  />
                  <Form.Label>Password</Form.Label>
                  <span className="password-info mt-2">
                    Use 8 or more characters with a mix of letters, numbers & symbols.
                  </span>
                </Form.Group>
                <Form.Group className="form-floating mb-3" controlId="floatingPassword">
                  <Form.Control
                    type="password"
                    placeholder="Password"
                    value={confirmPassword}
                    onChange={(event) => setConfirmPassword(event.target.value)}
                  />
                  <Form.Label>Confirm Password</Form.Label>
                </Form.Group>
                <Button type="submit" className="btn btn-success submit_btn w-100 mb-4">
                  Continue
                </Button>
                <div className="fw-normal text-muted">
                  Already have an account?{' '}
                  <a className="text-primary fw-bold text-decoration-none" style={{cursor: 'pointer'}} onClick={() => navigate("/login")}>
                    Sign in here
                  </a>
                </div>
              </Form>
            </div>
          </Col>
        </Row>
      </Container>
    </section>
  );
}

export default Signup;