<template>
  <v-container>
    <RouterLink :to="{ name: 'CreateArticleView' }"></RouterLink>
    <v-container class="text-center main-title pb-0">
      <h1>Financial Freedom Forum</h1>
    </v-container>
    <v-card class="my-5 mx-auto" max-width="100%">
      <v-row justify="end">
        <v-col cols="auto">
          <v-btn @click="createArticle" class="mt-5 me-10" color="yellow-darken-3" size="large" variant="tonal">New POST</v-btn>
        </v-col>
      </v-row>
      <v-list>
        <v-container class="pt-6 pb-0">
          <v-card class="border card-style mx-4">
            <v-row class="pb-0">
              <v-col cols="7">
                <p class="title-style ps-4">Title</p>
              </v-col>
              <v-col cols="2" class="">
                <p class="nick-style" style="text-align: center;">Nickname</p>
              </v-col>
              <v-col cols="3">
                <p class="date-style">Date</p>
              </v-col>
            </v-row>
          </v-card>
        </v-container>
        <v-list-item class="py-0" v-for="(item, index) in paginatedItems" :key="index">
          <v-list-item-content>
            <v-layout>
              <v-container fluid class="py-0">
                <v-card @click="detailView(item.id)" class="py-5 border card-hover card-style" density="compact">
                  <v-row>
                    <v-col cols="6">
                      <p class="link-style ps-4">{{ item.title }}</p>
                    </v-col>
                    <v-col cols="4" class="ps-16">
                      <v-row class="ms-16">
                        <v-col cols="2">
                          <v-avatar :image="`http://localhost:8000${item.user.profile_img}`" size="25" alt="User Profile Image"></v-avatar>
                        </v-col>
                        <v-col cols="10">
                          <p class="nick-color">{{ item.user.nickname }}</p>
                        </v-col>
                      </v-row>
                    </v-col>
                    <v-col cols="2">
                      <p class="date-color">{{ formatDate(item.created_at) }}</p>
                    </v-col>
                  </v-row>
                </v-card>
              </v-container>
            </v-layout>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-pagination class="" v-model="currentPage" :length="totalPages" @input="updatePagination"></v-pagination>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useArticleStore } from "@/stores/article";
import { RouterLink, useRouter } from "vue-router";
import { format } from "date-fns";
import { useUserStore } from "@/stores/user";
const userStore = useUserStore();
onMounted(() => {
  userStore.getProfile();
  console.log(userStore.userProfile.profile_img);
});
const profileImg = computed(() => {
  return `http://localhost:8000${userStore.userProfile.profile_img}`;
});
const router = useRouter();

const createArticle = function () {
  router.push({ name: "CreateArticleView" });
};

// 날짜 변환 함수
const formatDate = function (date) {
  return format(new Date(date), "yyyy-MM-dd");
};
const articleStore = useArticleStore();
onMounted(() => {
  articleStore.getArticleList();
});

watch(
  () => articleStore.articlesList,
  (newArticlesList) => {
    items.value = newArticlesList;
  }
);
const itemsPerPage = 5;
const items = ref([]);

const reversedItems = computed(() => {
  return [...items.value].reverse();
});
const currentPage = ref(1);

const totalPages = computed(() => {
  return Math.ceil(reversedItems.value.length / itemsPerPage);
});

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return reversedItems.value.slice(start, end);
});

const updatePagination = (page) => {
  currentPage.value = page;
};

const detailView = function (articleId) {
  router.push({ name: "ArticleDetailView", params: { id: articleId } });
};
</script>

<style>
.card-style {
  border-top: none !important;
  border-left: none !important;
  border-right: none !important;
  box-shadow: none !important;
  border-bottom: 1px solid black;
  border-radius: 0px !important;
}
.main-title {
  color: #9b7026;
}

.link-style {
  text-decoration: none;
  color: black;
  font-weight: 500;
}

.title-style {
  font-weight: 500;
  color: #f8a923;
}
.card-hover {
  transition: background-color 0s;
}

.card-hover:hover {
  background-color: #ffeed4; /* 원하는 배경색으로 변경 */
}

.nick-color {
  color: rgb(143, 143, 143);
}
.date-color {
  color: rgb(143, 143, 143);
  text-align: right;
  margin-right: 10px;
}

.nick-style {
  color: #f8a923;
  font-weight: 300;
}
.date-style {
  color: #f8a923;
  text-align: right;
  margin-right: 35px;
  font-weight: 300;
}
</style>
