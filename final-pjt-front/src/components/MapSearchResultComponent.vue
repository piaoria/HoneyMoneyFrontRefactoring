<template>
  <v-container>
    <v-row>
      <v-col v-for="result in results" :key="result.id" cols="6">
        <v-card class="mx-auto pb-2 custom-bg" @click="openDialog(result)">
          <v-card-title class="ibm-plex-sans-kr-regular">
            <h3>{{ result.fin_prdt_nm }}</h3>
          </v-card-title>
          <v-card-subtitle class="ibm-plex-sans-kr-regular">
            <h4>{{ result.kor_co_nm }}</h4>
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
    <v-dialog v-model="depositDialog" width="1000">
      <DepositDetailComponent @close-dialog="depositDialog = false" />
    </v-dialog>
    <v-dialog v-model="savingDialog" width="1000">
      <SavingDetailComponent @close-dialog="savingDialog = false" />
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, watch } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import swal from "sweetalert";
import { useRouter } from "vue-router";
import { useDepositStore } from "@/stores/deposit";
import { useSavingStore } from "@/stores/saving";
import DepositDetailComponent from "./DepositDetailComponent.vue";
import SavingDetailComponent from "./SavingDetailComponent.vue";
const depositDialog = ref(false);
const savingDialog = ref(false);

const depositStore = useDepositStore();
const savingStore = useSavingStore();
const router = useRouter();
const userStore = useUserStore();
const results = ref([]);

const props = defineProps({
  searchKeyword: String,
});

watch(
  () => props.searchKeyword,
  (newKeyword) => {
    if (!userStore.isLogin) {
      swal({
        title: "더 많은 정보를 보실래요?",
        text: "로그인 하시면 상품도 볼 수 있어요!",
        icon: "info",
        buttons: {
          cancel: "아뇨 괜찮아요",
          catch: {
            text: "로그인 하러 가기!",
          },
        },
      }).then((will) => {
        if (will) {
          router.push({ name: "LoginView" });
        }
      });
    } else {
      console.log(newKeyword);
      results.value = [];
      searchDeposit(newKeyword);
      searchSaving(newKeyword);
    }
  }
);

const searchDeposit = function (keyword) {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/products/bank/deposit/${keyword}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      res.data.forEach((element) => {
        results.value.push({
          ...element,
          type: "예금",
        });
      });
    })
    .catch((err) => {
      console.log("예금은 없어용");
    });
};

const searchSaving = function (keyword) {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/products/bank/saving/${keyword}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      res.data.forEach((element) => {
        results.value.push({
          ...element,
          type: "적금",
        });
      });
    })
    .catch((err) => {
      console.log("적금은 없어용");
    });
};

const openDialog = (result) => {
  if (result.type === "예금") {
    depositStore.getDepositData(result.fin_prdt_cd);
    depositStore.getDepositOptionData(result.fin_prdt_cd);
    depositDialog.value = true;
  } else if (result.type === "적금") {
    savingStore.getSavingData(result.fin_prdt_cd);
    savingStore.getSavingOptionData(result.fin_prdt_cd);
    savingDialog.value = true;
  }
};
</script>

<style scoped>
.custom-bg {
  background-color: #f8f0de;
}
</style>
