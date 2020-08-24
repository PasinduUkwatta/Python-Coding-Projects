import React, { Component } from "react";
import axios from "axios"

export default class Login extends Component {

    constructor(props) {
        super (props)

        this.state ={
            email: '',
            password: ''
        }
        this.changeHandler = this.changeHandler.bind(this);
        this.submitHandler = this.submitHandler.bind(this);
       
    }

    changeHandler = e => {
        this.setState({[e.target.name]: e.target.value})
    }

    submitHandler = e => {
        e.preventDefault()
        console.log(this.state)
        axios.post('/',this.state)
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            }
            
        )
this.props.history.push('/sign-up')
        }
    
  

    render() {
        const{email, password} = this.state

        return (
            <form onSubmit={this.submitHandler}  >
                <h3>Sign In</h3>

                <div className="form-group">
                    <label>Email address</label>
                    <input 
                    type="email" 
                    name ="email"
                    className="form-control" 
                    placeholder="Enter email" 
                    value={email} 
                    onChange={this.changeHandler}  />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input 
                    type="password" 
                    name="password"
                    className="form-control" 
                    placeholder="Enter password" 
                    value={password} 
                    onChange={this.changeHandler}  />
                </div>

                
                <button 
                type="submit" 
                className="btn btn-primary btn-block">
                Submit
                </button>
                
            </form>
        );
    }
}