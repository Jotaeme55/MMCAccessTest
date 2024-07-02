require('dotenv').config()
import axios from "axios"

export default class PaymentService {

    async getStripeSession(){
      
        try {
            const res = (await axios.post("/stripe")).data
            console.log(res)
            return res
        } catch (error) {
            console.log(error)
            return "error"
            
        }
    }

    async createProject(title,userId){
        const res = await axios.post("/index/project/"+title+"/"+userId)
        return res
    }

    async getProjectsFromUser(userId){
        const res = await axios.get("/index/project/"+userId)
        return res
    }

}