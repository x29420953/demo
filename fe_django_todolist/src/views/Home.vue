<template>
  <div class="home-box">
    <van-nav-bar
      title="ToDoList"
      right-text="新增"
      @click-right="onClickRight"
    />
    

    <div class="box-main">
      <a class="item" v-for="item in dataList" :key="item.id">
        <div class="lists">
          <router-link :to="{ name: 'Info', params: { id: item.id } }">
            <van-swipe-cell>
              <van-cell :border="false" :title="item.content"/>
              <template #right>
                <van-button square type="danger" text="刪除" />
              </template>
            </van-swipe-cell>
          </router-link>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { ajax } from "@/utils/ajax";
import { ToDoListApis } from "@/utils/apis";

export default {
  data() {
    return {
      dataList: [],
    };
  },
  methods: {
    getDataList() {
      ajax.get(ToDoListApis.ToDoListDetailUrl).then(({ data }) => {
        this.dataList = data.objects;
      });
    },
    onClickRight() {
      
    },
  },
  created() {
    this.getDataList();
  },
};
</script>
<style lang="less">
.home-box {
  padding: 0 10px;

  .box-main {
    width: 100%;
  }

  .item {
    
    .lists {
      background-color: rgba(170, 165, 165, 0.479);
      padding: 10px;
      margin-bottom: 10px;
      
    }
  }
}
</style>
