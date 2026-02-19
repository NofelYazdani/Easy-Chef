import { useState } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUtensils } from '@fortawesome/free-solid-svg-icons';
import './style.css'
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function Login() {
  const navigate = useNavigate();
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('phone', phone);
    formData.append('password', password);

    axios.post('http://127.0.0.1:8000/accounts/login/', formData)
      .then(response => {
        sessionStorage.setItem('token', response.data.access);
        navigate("/home");
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }

  return (
    <section className="vh-100">
      <Container fluid>
        <Row>
          <Col sm={6} className="text-black">
            <div className="px-5 ms-xl-4">
              <FontAwesomeIcon icon={faUtensils} className="fa-2x me-3 pt-5 mt-xl-4" />
              <a
                className="h1 fw-bold border-0 bg-white"
                style={{ textDecoration: 'none', color: 'black' }}
                type="button"
                onClick={() => navigate("/home")}
              >
                Easy Chef2
              </a>
            </div>

            <div className="d-flex align-items-center h-custom-2 px-5 ms-xl-4 mt-5 pt-5 pt-xl-0 mt-xl-n5">
              <Form className="rounded bg-white shadow p-5" onSubmit={handleSubmit} style={{width: 650}}>
                <h3 className="text-dark fw-bolder fs-4 mb-2">Login</h3>
                <Form.Group className="form-floating mb-3" controlId="floatingInput">
                  <Form.Control
                    type="tel"
                    placeholder="+12345678901"
                    // pattern="[0-9]{3}[0-9]{3}[0-9]{4}"
                    value={phone}
                    onChange={(event) => setPhone(event.target.value)}
                  />
                  <Form.Label>Phone number</Form.Label>
                </Form.Group>
                <Form.Group className="form-floating mb-3" controlId="floatingPassword">
                  <Form.Control type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
                  <Form.Label>Password</Form.Label>
                </Form.Group>
                <Button type="submit" className="btn btn-primary submit_btn w-100 my-4">
                  Continue
                </Button>
                <div className="fw-normal text-muted mb-2">
                  Don't have an account?{' '}
                  <a className="text-primary fw-bold text-decoration-none" style={{cursor: 'pointer'}} onClick={() => navigate("/")}>
                    Register here
                  </a>
                </div>
              </Form>
            </div>
          </Col>
          <Col sm={6} className="px-0 d-none d-sm-block">
            <img
              src={require('./background02.jpg')}
              alt="Login image"
              className="w-100 vh-100"
              style={{ objectFit: 'cover', objectPosition: 'right' }}
            />
          </Col>
        </Row>
      </Container>
    </section>
  );
}

export default Login;