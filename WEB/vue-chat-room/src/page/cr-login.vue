<template>
    <div class="login">
        <div class="back"></div>
        <el-card class="box-card">
            <div class="user-box">
                <img src="@/assets/logo.png"/>
                <strong>Gilfoyle</strong>
                <el-input v-model="psw" placeholder="嘤嘤嘤"/>
            </div>
        </el-card>
    </div>
</template>

<script>

export default{
    name:"cr-login",
    data(){
        return {
            psw:""
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
    border: 1px solid gray;
}

.user-box>*{
    margin-top: 30px;
}
.el-input{
    width: 50%;
}

.box-card {
  width: 480px;
  z-index: 1;
  border-radius: 5px;
  background: rgba(255, 255, 255, .5);
  box-shadow: 3px 3px 6px 3px rgba(0, 0, 0, .3);
  min-height: 300px;
}

</style>