<template>
    <section class="container" :class="{'menu-open': menuOpen}" > <!--最外层容器-->
    <section class="menu"> <!--左边的容器-->
      <menus></menus>
    </section>
      <div class="content-overlay" @click="$store.dispatch('updateMenu')"></div>
    <section class="content-container"><!--右边的容器-->
    <todo></todo>
    </section>
  </section>
</template>

<script>
  import menus from './menus';
  import todo from './todo';
  export default {
    components:{
      menus,
      todo
    },
    computed:{
      menuOpen(){
        return this.$store.state.menuOpen;
      }

    }
    }
</script>

<style lang="less">
@import '../common/style/layouts.less';
</style>
