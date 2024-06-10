<template>
  <v-container class="py-0 mb-0" v-if="savingStore.profileSavingData.length">
    <v-row class="ms-12 mb-1" justify="end">
      <v-badge class="badge-style" color="yellow" :content="savingStore.profileSavingData.length"></v-badge>
      <v-img class="mb-0 me-2" :src="jar" max-width="45"></v-img>
      <v-row class="py-0 my-0" align="end">
        <v-col class="mx-0 py-0 my-0 px-0" cols="7">
          <h2 class="ms-1 font-weight-black ibm-plex-sans-kr-regular">
            담아둔
            <span class="span-text">적금</span>
          </h2>
        </v-col>
      </v-row>
    </v-row>
    <v-carousel v-model="currentSlide" height="300" show-arrows="hover" hide-delimiters>
      <v-carousel-item v-for="(honeySaving, index) in savingStore.profileSavingData" :key="`carousel2-${index}`" class="no-padding">
        <v-card class="mx-16 fill-height d-flex align-center justify-center" elevation="0">
          <v-card class="card-design mb-2 density-compact" :prepend-avatar="getBankIcon(honeySaving.kor_co_nm)" variant="text">
            <template v-slot:subtitle>
              <span class="ibm-plex-sans-kr-regular">{{ honeySaving.kor_co_nm }}</span>
            </template>
            <template v-slot:title>
              <span class="font-weight-black ibm-plex-sans-kr-regular">
                <h4>{{ honeySaving.fin_prdt_nm }}</h4>
              </span>
              <v-spacer></v-spacer>
              <v-btn class="absolute-btn" elevation="0" icon @click="removeSavingCard(honeySaving)">
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </template>
            <template v-if="savingLoding">
              <v-card-text class="mt-3 pb-0 ibm-plex-sans-kr-regular d-flex justify-center">
                <v-progress-linear color="yellow-darken-2" indeterminate></v-progress-linear>
              </v-card-text>
            </template>
            <v-card-text class="mt-3 pb-0 ibm-plex-sans-kr-regular">가입 방법 : {{ honeySaving.join_way }}</v-card-text>
            <v-card-text class="ibm-plex-sans-kr-regular">만기 후 이자율 : {{ honeySaving.mtrt_int }}</v-card-text>
            <v-container align="center">
              <v-btn color="yellow-darken-3" variant="tonal" @click="viewDetailSaving(honeySaving)">Details</v-btn>
            </v-container>
          </v-card>
        </v-card>
      </v-carousel-item>
    </v-carousel>
    <!-- saving dialog -->
    <v-dialog v-model="savingDialog" width="1000">
      <ProfileUserSavingDetailComponent @close-dialog="savingDialog = false" />
    </v-dialog>
  </v-container>
  <v-container v-else>
    <v-container class="my-6 py-6 ibm-plex-sans-kr-regular" align="center" justify="center">
      <v-img width="100" :src="empty"></v-img>
      <p class="gray-text">적금 꿀통이 비어있어요...</p>
      <v-btn @click="goSaving" color="yellow-darken-2 mt-4" size="large" variant="tonal">
        <p class="ibm-plex-sans-kr-regular bold-text">적금 꿀 바르러 가기!</p>
      </v-btn>
    </v-container>
  </v-container>
</template>

<script setup>
import { ref, watch } from "vue";
import { storeToRefs } from "pinia";
import { useUserStore } from "@/stores/user";
import { useSavingStore } from "@/stores/saving";
import jar from "@/assets/jar.png";
import empty from "@/assets/empty.png";
import { useRouter } from "vue-router";
import ProfileUserSavingDetailComponent from "@/components/ProfileUserSavingDetailComponent.vue";
import Kyungnam from "@/assets/bank/Kyungnam.jpg";
import Gwangju from "@/assets/bank/Gwangju.jpg";
import Kookmin from "@/assets/bank/Kookmin.jpg";
import Nonghyup from "@/assets/bank/Nonghyup.jpg";
import Daegu from "@/assets/bank/Daegu.jpg";
import Busan from "@/assets/bank/Busan.jpg";
import Suhyup from "@/assets/bank/Suhyup.jpg";
import StandardChartered from "@/assets/bank/StandardChartered.jpg";
import Shinhan from "@/assets/bank/Shinhan.jpg";
import Woori from "@/assets/bank/Woori.jpg";
import Jeonbuk from "@/assets/bank/Jeonbuk.jpg";
import Jeju from "@/assets/bank/Jeju.jpg";
import IBK from "@/assets/bank/IBK.jpg";
import Kakao from "@/assets/bank/Kakao.jpg";
import Kbank from "@/assets/bank/Kbank.png";
import Toss from "@/assets/bank/Toss.jpg";
import Hana from "@/assets/bank/Hana.jpg";
import KDB from "@/assets/bank/KDB.jpg";

const bankIcon = {
  경남은행: Kyungnam,
  광주은행: Gwangju,
  국민은행: Kookmin,
  농협은행주식회사: Nonghyup,
  대구은행: Daegu,
  부산은행: Busan,
  수협은행: Suhyup,
  한국스탠다드차타드은행: StandardChartered,
  신한은행: Shinhan,
  우리은행: Woori,
  전북은행: Jeonbuk,
  제주은행: Jeju,
  중소기업은행: IBK,
  "주식회사 카카오뱅크": Kakao,
  "주식회사 케이뱅크": Kbank,
  "토스뱅크 주식회사": Toss,
  하나은행: Hana,
  한국산업은행: KDB,
};

const getBankIcon = function (korCoNm) {
  return bankIcon[korCoNm] || "defaultIcon";
}; // 기본 아이콘 설정 가능

const router = useRouter();
const savingLoding = ref(false);
const savingStore = useSavingStore();
const userStore = useUserStore();

const { userProfile } = storeToRefs(userStore);

const currentSlide = ref(0);

watch(savingStore.profileSavingData, (newValue, oldValue) => {
  if (currentSlide.value >= newValue.length) {
    currentSlide.value = newValue.length > 0 ? newValue.length - 1 : 0;
  }
});
// 꿀바른 상품 확인 함수
const checkSaving = function () {
  savingStore.getProfileSaving(userProfile.value.interest_saving);
};

const savingDialog = ref(false);

const viewDetailSaving = function (savingData) {
  savingStore.getSavingData(savingData.fin_prdt_cd);
  savingStore.getSavingOptionData(savingData.fin_prdt_cd);
  savingDialog.value = true;
};

const goSaving = function () {
  router.push({ name: "SavingProductsView" });
};

const removeSavingCard = function (removeSavingData) {
  savingLoding.value = true;
  setTimeout(() => {
    savingLoding.value = false;
  }, 1000);
  // 카드 삭제 로직
  savingStore.getHoney(removeSavingData.fin_prdt_cd);
  savingStore.toggleData(removeSavingData);
  checkSaving();
  // 강제로 carousel 리렌더링하면서 v-model 값을 변경시켜 cardpage를 변경
  if (currentSlide.value > 0) {
    currentSlide.value -= 1;
  }
};
</script>

<style scoped>
.card-design {
  border-radius: 8px;
  background-color: rgba(253, 248, 222, 0.658);
}

.absolute-btn {
  position: absolute;
  background-color: #ffffff00;
  font-size: 15px;
  top: 15px; /* 카드 위쪽에서의 거리 조절 */
  right: 15px; /* 카드 오른쪽에서의 거리 조절 */
  width: 25px; /* 버튼의 너비 조절 */
  height: 25px; /* 버튼의 높이 조절 */
}
.gray-text {
  color: rgba(159, 159, 159, 0.579);
  font-size: larger;
}

.bold-text {
  font-weight: bold;
}
.span-text {
  color: #e28000a9;
}
</style>
