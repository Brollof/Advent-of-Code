#include <iostream>
#include <openssl/md5.h>

static bool is_five(const uint8_t *hash)
{
  return hash[0] == 0x00 && hash[1] == 0x00 && (hash[2] >> 4) == 0x00;
}

static bool is_six(const uint8_t *hash)
{
  return is_five(hash) && hash[2] == 0;
}

static void print_md5(const uint8_t *md5)
{
  for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
  {
    printf("%02x", md5[i]);
  }
  printf("\n");
}

int main()
{
  uint8_t result[MD5_DIGEST_LENGTH];
  const std::string secret("iwrupvqb");
  uint32_t i = 0;
  
  do
  {
    i++;
    std::string s = secret + std::to_string(i);
    MD5((const uint8_t *)s.c_str(), s.size(), result);
  } while (is_five(result) == false);
  std::cout << i << std::endl;

  i = 0;
  do
  {
    i++;
    std::string s = secret + std::to_string(i);
    MD5((const uint8_t *)s.c_str(), s.size(), result);
  } while (is_six(result) == false);
  std::cout << i << std::endl;

  return 0;
}

