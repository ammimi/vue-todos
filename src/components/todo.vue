<template>
  <div class="page lists-show">
    <!-- 头部模块 -->
    <nav>
      <!-- 当用户浏览车窗口尺寸小于40em时候，显示手机端的菜单图标 -->
      <div class="nav-group">
        <a class="nav-item">
          <span class="icon-list-unordered">
          </span>
        </a>
      </div>
      <!-- 显示标题和数字模块 -->
      <h1 class="title-page">
        <span class="title-wrapper">{{todo.title}}</span>  <!-- title:标题 绑定标题 -->
        <span class="count-list">{{todo.count || 0}}</span><!-- count:数量 绑定代办单项熟练-->
      </h1>
      <!-- 右边显示删除图标和锁定图标的模块 -->
      <div class="nav-group right">
        <div class="options-web">
          <a class=" nav-item">
            <!-- cicon-lock锁定的图标
            icon-unlock：非锁定的图标
            -->
            <span class="icon-lock" v-if="todo.locked"></span>
            <span class="icon-unlock" v-else>
            </span>
          </a>
          <a class=" nav-item">
            <span class="icon-trash">
            </span>
          </a>
        </div>
      </div>
      <!-- 用户新增代办事项的input模块 -->
      <div class=" form todo-new input-symbol">
        <!-- 绑定disabled值，当todo.locked为绑定的时候，禁止input输入 -->
        <input type="text" v-model="text" placeholder='请输入' :disabled="todo.locked" />
        <span class="icon-add"></span>
      </div>
    </nav>
    <!-- 列表主体模块 -->
    <div class="content-scrollable list-items">
    <div v-for="item in items">
        <item :item="item"></item>
      </div>
    </div>
  </div>
</template>

<script>
// 引入组件
import item from './item';
import { getTodo} from '../api/api';

  export default {
   components: {
    item
  },
   watch: {
    '$route.params.id'() {
    // 监听$route.params.id的变化，如果这个id即代表用户点击了其他的待办项需要重新请求数据。
      this.init();
    }
  },
  created() {
  // created生命周期，在实例已经创建完成，页面还没渲染时调用init方法。
    this.init();
  },
  methods: {
    init() {
    // 获取到 $route下params下的id,即我们在menus.vue组件处传入的数据。
      const ID = this.$route.params.id;
      getTodo({ id: ID }).then(res => {

        let { id, title, count, isDelete, locked, record
        } = res.data.todo;
        // 请求成功，拿到res.data.todo;在将record 赋值到代办单项列表，其它数据赋值到todo对象
        this.items = record;
        this.todo = {
          id: id,
          title: title,
          count: count,
          locked: locked,
          isDelete: isDelete
        };
      });
    }
},
  data() {
    return {
      todo: {
        title: '星期一', //标题
        count: 12, //数量
        locked: false //是否绑定
      },
      items: [  //代办单项列表
      ],
      text: '' //用户输入单项项绑定的输入
    }
  }
}
</script>

<style lang="less">
  @import '../common/style/nav.less';
  @import '../common/style/form.less';
  @import '../common/style/todo.less';
</style>
