<template>
  <div class="info-box">
    <van-nav-bar
      title="ToDoList"
      left-text="返回"
      left-arrow
      fixed
      @click-left="goBack"
    />
    <div class="box-main">
      <a class="item" v-for="item in dataList" :key="item.id">
        <div class="list">
            {{ item.content }}
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
      id: "",
      dataList: [],
    };
  },
  methods: {
    getDataList() {
      const url = ToDoListApis.ToDoListDetailUrl.replace("#{id}", this.id);
      ajax.get(url).then(({ data }) => {
        this.dataList = data.objects;
      });
    },
    goBack() {
      this.$router.go(-1);
    }
  },
  created() {
    this.id = this.$route.params.id;
    this.getDataList();
  },
};
</script>
<style lang="less">
.info-box {
  padding: 0 10px;

  .box-main {
    width: 100%;
  }

  .item {
    .list {
      background-color: rgba(170, 165, 165, 0.479);
      padding: 10px;
      padding-top: 50px;
      padding-bottom: 10px;
      margin-bottom: 10px;
    }
  }
}
</style>
