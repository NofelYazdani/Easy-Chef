import { useState } from "react";
import './style.css';
import React from 'react';
import {
    Container,
    Row,
    Col,
    Card,
    Carousel,
    Form,
    Button,
    InputGroup,
    Navbar,
    Nav,
    NavDropdown,
    FormControl
} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

const App = () => {
    return (
        <>
            <header className="masthead">
                <div className="container px-4 px-lg-5 d-flex h-100 align-items-center justify-content-center">
                    <div className="d-flex justify-content-center">
                        <div className="text-center">
                            <h1 className="mx-4 my-0 text-uppercase">Easy Chef</h1>
                            <h2 className="text-white-50 mx-auto mt-2 mb-5">Elevate Your Cooking Game with Easy Chef - Your Recipe Hub.</h2>
                            <Button variant="success" href="../recipe_search/recipe_search.html">Browse Recipes</Button>
                        </div>
                    </div>
                </div>
            </header>

            <Container fluid className="about-section text-center" id="about">
                <Row className="justify-content-center">
                    <Col lg={8}>
                        <h2 className="text-white mb-4">What our website has to offer</h2>
                        <p className="text-white-50">
                            With Easy Chef, you can search through millions of different recipes from various diets and
                            ingredients from all over the world! You can also share your custom recipe with everyone! You
                            don't need to worry about the shopping list either; Easy Chef takes care of that as well!
                        </p>
                    </Col>
                </Row>
                <Row className="justify-content-center">
                    <Col lg={6} className="d-flex justify-content-center">
                        <img src={require("./white.png")} alt="..." className="img-fluid" width="525" height="525" />
                    </Col>
                </Row>
            </Container>

            <Navbar bg="transparent" expand="lg" fixed="top" className="position-absolute" id="mainNav">
                <Container fluid>
                    <Navbar.Brand className="mx-5">Easy Chef</Navbar.Brand>
                    <Navbar.Toggle aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation" />
                    <Navbar.Collapse id="navbarResponsive">
                        <Nav className="ms-auto">
                            <Nav.Link href="../recipe-create/recipe-creating.html">Create Recipe</Nav.Link>
                            <Nav.Link href="./login">Login</Nav.Link>
                            <NavDropdown title="Account" id="navbarDropdownMenuLink">
                                <NavDropdown.Item href="../Profile/profile_page.html">View Profile</NavDropdown.Item>
                                <NavDropdown.Item href="../my_recipes/my_recipes.html">My Recipes</NavDropdown.Item>
                                <NavDropdown.Item href="../shopping_list/shopping_list.html">Shopping List</NavDropdown.Item>
                                <NavDropdown.Item href="../login/login.html">Logout</NavDropdown.Item>
                            </NavDropdown>
                            <Form className="d-flex">
                                <Nav.Item>
                                    <div className="d-flex justify-content-center mx-5">
                                        <div className="searchbar">
                                            <input className="search_input" type="text" placeholder="Search..." />
                                            <a href="#" className="search_icon"><FontAwesomeIcon icon={faSearch} /></a>
                                        </div>
                                    </div>
                                </Nav.Item>
                            </Form>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            {/* Projects */}
            <section
                className="projects-section bg-dark bg-opacity-10"
                id="projects"
            >
                <h1
                    className="text-uppercase"
                    style={{ textAlign: 'center', paddingBottom: '2%' }}
                >
                    Top Recipes
                </h1>
                <Container className="w-50 vh-75">
                    {/* Featured Project Row */}
                    <Row className="gx-0 mb-4 mb-lg-5 align-items-center">
                        <Col>
                            <Carousel>
                                <Carousel.Item>
                                    <a href="../detailed_recipe/recipe.html">
                                        <img
                                            src={require("./cheesecakepic.jpeg")}
                                            className="d-block w-100"
                                            alt="..."
                                        />
                                    </a>
                                    <Carousel.Caption className="d-none d-md-block bg-success">
                                        <h5>Strawberry Cream Cheesecake</h5>
                                        <p>15 Minutes</p>
                                    </Carousel.Caption>
                                </Carousel.Item>
                                <Carousel.Item>
                                    <a href="../detailed_recipe/recipe.html">
                                        <img
                                            src={require("./cheesecakepic.jpeg")}
                                            className="d-block w-100"
                                            alt="..."
                                        />
                                    </a>
                                    <Carousel.Caption className="d-none d-md-block bg-success">
                                        <h5>Strawberry Cream Cheesecake</h5>
                                        <p>15 Minutes</p>
                                    </Carousel.Caption>
                                </Carousel.Item>
                                <Carousel.Item>
                                    <a href="../detailed_recipe/recipe.html">
                                        <img
                                            src={require("./cheesecakepic.jpeg")}
                                            className="d-block w-100"
                                            alt="..."
                                        />
                                    </a>
                                    <Carousel.Caption className="d-none d-md-block bg-success">
                                        <h5>Strawberry Cream Cheesecake</h5>
                                        <p>15 Minutes</p>
                                    </Carousel.Caption>
                                </Carousel.Item>
                            </Carousel>
                        </Col>
                    </Row>
                </Container>
            </section>
            {/* Signup */}
            <section className="signup-section" id="signup">
                <Container>
                    <Row>
                        <Col md={{ span: 10, offset: 1 }} lg={{ span: 8, offset: 2 }} className="mx-auto text-center">
                            <i className="far fa-paper-plane fa-2x mb-2 text-white"></i>
                            <h2 className="text-white mb-5">
                                Subscribe to receive updates!
                            </h2>
                            <Form>
                                {/* Email address input */}
                                <Row>
                                    <Col>
                                        <InputGroup className="mb-3">
                                            <Form.Control
                                                type="email"
                                                placeholder="Enter email address..."
                                                aria-label="Enter email address..."
                                            />
                                            <Button variant="success" type="submit">
                                                Notify Me!
                                            </Button>
                                        </InputGroup>
                                    </Col>
                                </Row>
                            </Form>
                        </Col>
                    </Row>
                </Container>
            </section>
            {/* Contact */}
            <section className="contact-section bg-dark">
                <Container>
                    <Row>
                        <Col md={4}>
                            <Card className="py-4 h-100">
                                <Card.Body className="text-center">
                                    <i
                                        className="fas fa-map-marked-alt text-primary mb-2"
                                        style={{ color: '#568203 !important' }}
                                    ></i>
                                    <h4 className="text-uppercase m-0">Address</h4>
                                    <hr className="my-4 mx-auto" />
                                    <div className="small text-black-50">
                                        3359 Mississauga Rd, Ontario, Canada
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col md={4}>
                            <Card className="py-4 h-100">
                                <Card.Body className="text-center">
                                    <i
                                        className="fas fa-envelope text-primary mb-2"
                                        style={{ color: '#568203 !important' }}
                                    ></i>
                                    <h4 className="text-uppercase m-0">Email</h4>
                                    <hr className="my-4 mx-auto" />
                                    <div className="small text-black-50">
                                        <a href="#!">easychef@cook.com</a>
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col md={4}>
                            <Card className="py-4 h-100">
                                <Card.Body className="text-center">
                                    <i
                                        className="fas fa-mobile-alt text-primary mb-2"
                                        style={{ color: '#568203 !important' }}
                                    ></i>
                                    <h4 className="text-uppercase m-0">Phone</h4>
                                    <hr className="my-4 mx-auto" />
                                    <div className="small text-black-50">
                                        +1 (437) 344-4993
                                    </div>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>
                    <Row className="justify-content-center">
                        <Col className="d-flex justify-content-center">
                            <a className="mx-2" href="#!">
                                <i className="fab fa-twitter"></i>
                            </a>
                            <a className="mx-2" href="#!">
                                <i className="fab fa-facebook-f"></i>
                            </a>
                            <a className="mx-2" href="#!">
                                <i className="fab fa-instagram"></i>
                            </a>
                        </Col>
                    </Row>
                </Container>
            </section>
            {/* Footer */}
            <footer className="footer bg-dark small text-center text-white-50">
                <Container>Copyright © Easy Chef 2023</Container>
            </footer>
        </>
    );

}

export default App;