<template>
    <div class="main">
        <nav>
            <img src="@/assets/logo.png"/>
            <h1>在线聊天</h1>
        </nav>
        <div class="block text-center" m="t-4">
            <el-carousel trigger="click" height="200px">
                <el-carousel-item v-for="item in 4" :key="item">
                    <h3 class="small justify-center" text="2xl">{{ item }}</h3>
                </el-carousel-item>
            </el-carousel>
        </div>
        <el-scrollbar>
            <div class="content">
                <el-card :body-style="{ padding: '0px' }" v-for="i in 5" :key="i">
                    <img
                        src="@/assets/register.jpg"
                        class="image"
                    />
                    <div style="padding: 14px">
                        <span>嘤嘤嘤</span>
                        <div class="bottom">
                            <time class="time">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores cum eligendi voluptate molestias vitae illum placeat. Sit odio doloremque similique.</time>
                            <el-button text class="button" @click="goto" style="margin-right:0px;">进入房间</el-button>
                        </div>
                    </div>
                </el-card>
            </div>   
        </el-scrollbar>
    </div>
</template>

<script>
import {ElCarousel,ElCarouselItem} from "element-plus";


export default{
    components:{
        ElCarousel,ElCarouselItem
    },
    methods:{
        goto(){
            this.$router.push('/chat');
        }
    }
}


</script>


<style scoped>

.main{
    width: 100%;
    height: 100%;
    background-color: #F5F7F9;
    display: flex;
    flex-direction: column;
    justify-content: center;    
}
nav{
    background-color: #909399;
    height: 80px;
    overflow: hidden;
    display: flex;
    align-items: center;
}
nav>img{
    width: 45px;
    height: 45px;
    margin-left: 30px;
}
nav>h1{
    color: white;
    margin-left: 10px;
}


.demonstration {
  color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.content{
    flex: 1;
    column-count: 2;
    column-gap: 5px;
    padding: 5px;
}
.el-card{
    margin-bottom: 5px;
}
.el-scrollbar{
    height: 100%;
}

</style>

<style>
.time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  align-items: flex-end;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}
</style>
