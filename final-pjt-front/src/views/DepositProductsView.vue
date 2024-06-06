<template>
  <v-container>
    <v-container class="d-flex justify-end">
      <v-col class="my-0 py-0" cols="5">
        <v-select class="ibm-plex-sans-kr-regular" v-model="bank" :items="depositStore.bankList" label="은행" variant="outlined"></v-select>
      </v-col>
    </v-container>
    <v-data-table-virtual height="600" :items="depositData" class="elevation-2" item-class="hoverable-row" fixed-header>
      <!-- userPeriod에 따라 다른 기간을 선택하여 표시 -->
      <template v-if="userPeriod && userPeriod === 6" v-slot:item.6개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 12" v-slot:item.12개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 24" v-slot:item.24개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else-if="userPeriod && userPeriod === 36" v-slot:item.36개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-else v-slot:item.6개월="{ value }">
        <v-chip :color="getColor(value)">{{ value }}</v-chip>
      </template>
      <template v-slot:item.상품명="{ item }">
        <v-btn class="mx-auto custom-btn" @click="showDetails(item.상품명)">{{ item.상품명 }}</v-btn>
      </template>
    </v-data-table-virtual>
    <v-dialog v-model="dialog" width="1000">
      <DepositDetailComponent @close-dialog="dialog = false" />
    </v-dialog>
  </v-container>
</template>

<script setup>
import { useDepositStore } from "@/stores/deposit";
import { onMounted, watch, ref } from "vue";
import { useUserStore } from "@/stores/user";
import DepositDetailComponent from "@/components/DepositDetailComponent.vue";
const userStore = useUserStore();
const depositStore = useDepositStore();
const depositData = ref([]);
const dialog = ref(false);

const loaddata = function () {
  let i = 1;
  if (depositStore.allDeposit && depositStore.allDeposit.length > 0) {
    depositData.value = depositStore.allDeposit.map((element) => {
      const option6 = element.depositoption_set.find((option) => option.save_trm === 6);
      const intrRate6 = option6 ? option6.intr_rate : null;
      const option12 = element.depositoption_set.find((option) => option.save_trm === 12);
      const intrRate12 = option12 ? option12.intr_rate : null;
      const option24 = element.depositoption_set.find((option) => option.save_trm === 24);
      const intrRate24 = option24 ? option24.intr_rate : null;
      const option36 = element.depositoption_set.find((option) => option.save_trm === 36);
      const intrRate36 = option36 ? option36.intr_rate : null;
      return {
        NO: i++,
        상품코드: element.fin_prdt_cd,
        은행: element.kor_co_nm,
        상품명: element.fin_prdt_nm,
        "6개월": intrRate6,
        "12개월": intrRate12,
        "24개월": intrRate24,
        "36개월": intrRate36,
      };
    });
  }
};
onMounted(() => {
  depositStore.getAllDeposit();
});
watch(
  () => depositStore.allDeposit,
  () => {
    loaddata();
  },
  { immediate: true }
);

const bank = ref("은행을 선택해 보세요!");

watch(bank, () => {
  loaddata();
  if (bank.value !== "모든은행") {
    depositData.value = depositData.value.filter((item) => {
      return item.은행 === bank.value;
    });
  }
});

const showDetails = (productName) => {
  findDetail(productName);
  dialog.value = true;
};

const findDetail = function (productName) {
  depositStore.getDepositData(productName);
  depositStore.getDepositOptionData(productName);
};

// getColor 함수 정의
const getColor = (value) => {
  if (value >= 3) {
    return "green";
  } else if (value >= 2) {
    return "orange";
  } else {
    return "white";
  }
};
const userPeriod = userStore.userProfile.desirePeriod;
</script>

<style scoped>
.hoverable-row {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hoverable-row:hover {
  background-color: #f5f5f5;
}
</style>
