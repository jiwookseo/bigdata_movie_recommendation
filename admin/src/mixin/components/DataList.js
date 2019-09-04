export default {
  data() {
    return {
      index: 1,
      currentPage: 1
    }
  },
  computed: {
    pageArray() {
      const pages = []
      for (let i = this.index; i < this.index + 10; i++) {
        pages.push(i)
      }
      return pages
    },
    numberOfData() {
      return this.dataList.length;
    },
    lastPage() {
      let lastPageNumber = parseInt(this.numberOfData / 10);
      if (this.numberOfData % 10) {
        lastPageNumber += 1;
      }
      return lastPageNumber
    },
    lastIndex() {
      let lastIndexNumber = parseInt(this.numberOfData / 100)*10;
      if (this.numberOfData % 100) {
        lastIndexNumber += 1;
      } else {
        lastIndexNumber -= 9;
      }
      return lastIndexNumber
    }
  },
  methods: {
    // Test Log : console.log(this.numberOfData, this.index, this.currentPage, this.lastPage, this.lastIndex);
    showFirstPageList() {
      if (this.index > 1) {
        this.index = 1;
        this.currentPage = this.index;
      }
    },
    showLastPageList() {
      if (this.index + 10 <= this.lastIndex) {
        this.index = this.lastIndex;
        this.currentPage = this.lastPage;
      }
    },
    showPrevPageList() {
      if (this.index > 1) {
        this.index -= 10;
        this.currentPage = this.index;
      }
    },
    showNextPageList() {
      if (this.index + 10 <= this.lastIndex) {
        this.index += 10;
        this.currentPage = this.index;
      }
    },
    changeCurrentPage(pageNumber) {
      this.currentPage = this.index + (pageNumber - this.index);
    }
  }
}