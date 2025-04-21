void mulvec(int *dst, int *src1, int *src2, int N) {
  for (int i = 0; i < N; i++)
    dst[i] = src1[i] * src2[i];
}
