<template>
    <div class="login">
        <div class="back"></div>
        <el-card class="box-card">
            <div class="user-box">
                <img src="@/assets/logo.png"/>
                <strong>Gilfoyle</strong>
                <div class="wrapper">
                    <div class="input-data">
                        <input type="text" required="" v-model="psw"/>
                        <div class="underline"></div>
                        <label>用户名</label>
                    </div>
                </div>
                <el-button :style="show" @click="login" :icon="Check" size="large" circle/>
            </div>
        </el-card>
    </div>
</template>

<script>
import {
    Check
} from '@element-plus/icons-vue'


export default{
    name:"cr-login",
    data(){
        return {
            psw:"",
            Check
        }
    },
    computed:{
        show(){
            if(this.psw){
                return `visibility: visible;`;
            }
            return `visibility: hidden;`;
        }
    },
    methods:{
        login(){
            this.$router.push('/main');
        }
    }
}

</script>

<style scoped>

.login{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    
}

.back{
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: url("@/assets/register.jpg");
    -moz-background-size:100% 100%;
    background-size:100% 100%;
    filter: blur(0px);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.user-box{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.user-box>img{
    width: 100px;
    border-radius: 50px;
    border: 1px solid #572e2e;
}

.user-box>*{
    margin-top: 30px;
}
.user-box>.el-button{
    margin-top: 0;
    transition-delay: 300ms;
}

.el-input{
    width: 50%;
}

.user-box>>>.el-input__wrapper{
    border-radius: 12px;
}

.box-card {
  width: 480px;
  z-index: 1;
  border-radius: 5px;
  background: rgba(255, 255, 255, .5);
  box-shadow: 3px 3px 6px 3px rgba(0, 0, 0, .3);
  min-height: 300px;
}


.wrapper{
    width: 50%;
    background-color: rgba(0,0,0,0);
    padding: 30px;
    /* box-shadow: 0px 0px 10px rgba(0,0,0,0.1); */
}
.wrapper .input-data{
    width: 100%;
    height: 40px;
    position: relative;
}
.wrapper .input-data input{
    width: 100%;
    height: 100%;
    border: none;
    border-bottom: 2px solid silver;
    font-size: 17px;
    background-color: rgba(255,255,255,0.9);
    outline: none;
}
.input-data input:focus ~ label,
.input-data input:valid ~ label{
    transform: translateY(-20px);
    font-size: 15px;
    color: #572e2e;
}
.wrapper .input-data label{
    position: absolute;
    bottom: 10px;
    left: 0;
    color: grey;
    pointer-events: none;
    transition: all 0.3s ease;
}
.wrapper .input-data .underline{
    position: absolute;
    bottom: 0px;
    height: 2px;
    width: 100%;
}
.input-data .underline:before{
    position: absolute;
    content: "";
    height: 100%;
    width: 100%;
    background: #572e2e;
    transform: scaleX(0);
    transition:transform 0.3s ease;
}

.input-data input:focus ~ .underline:before,
.input-data input:valid ~ .underline:before{
    transform: scaleX(1);
}

</style>
