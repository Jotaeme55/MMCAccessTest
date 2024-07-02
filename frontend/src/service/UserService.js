import axios from 'axios';
const CryptoJS = require('crypto-js')
require('dotenv').config()
// import dotenv from 'dotenv';
// import path from 'path';
const palabra_secreta_aes = process.env.VUE_APP_SECRET_WORD_AES
// dotenv.config({ path: path.resolve(__dirname, '../../.env') });
export default class UserService {

    async sendUserQuestionToBeelasy(name,message,email){
        return axios.post('/sendEmail',{name,message,email})
    }

    async saveUser(user) {
        return axios.post('/users/', user);
    }

    async getUser(email) {
        try {
          const response = await axios.get(`/users/${email}`);
          return response.data;
        } catch (error) {
          console.error(`Error retrieving user ${email}: ${error}`);
          return null;
        }
      }

    async guardar(user,code){
        return axios.post(`auth/register/${code}`,user)
        .then((response) => response.data)
        .catch((e)=>{
            console.error('error' + e);
        });
    }

    async actualizar(userId,user){
        return axios.put(`users/${userId}`,user)
        .then((response) => response.data)
        .catch((e)=>{
            console.error('error' + e);
        });
    }

    async deleteUser(userID, token) {
        const config = {
          headers: {
            authorization: `Bearer ${token}`
          }
        };
      
        try {
          const response = await axios.delete(`/users/${userID}`, config);
          return response.data;
        } catch (error) {
          console.error('Error:', error);
        }
      }


    async sendIndexAndStyle(userID, token, indice, estilo) {
     
      const headers= {
          authorization: 'Bearer ' + token
        }
      const responseType = "arraybuffer"
      
      const body = {"index":indice, "estilo":estilo}
      try {
        const response = await axios.post(`/index/${userID}`,body , {headers, responseType}, );
        return response.data;
      } catch (error) {
        console.error('Error:', error);
      }
    }

    async generateCode(email){
        return axios.get(`/sendConfirmation/${email}`)
        .then((response) => response)
        .catch((e)=>{
            console.error('error' + e);
        });
    }

    async sendCode(email,code){
        return axios.get(`/sendConfirmation/email/${email}/code/${code}`)
        .then((response) => response)
        .catch((e)=>{
            console.error('error' + e);
        });
    }

    async sendGoogleCode(code){
        return axios.post(`/auth/google`,{code})
        .then((response) => response)
        .catch((e)=>{
            console.error('error' + e);
        });
    }

    descifrarUsuarioYGuardar(data){
        return CryptoJS.AES.decrypt(data, palabra_secreta_aes).toString(CryptoJS.enc.Utf8);
    }
}