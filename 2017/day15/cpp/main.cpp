#include <iostream>

uint32_t part1(uint64_t a, uint64_t b)
{
  uint32_t res = 0;
  for (int i = 0; i < 40000000; i++)
  {
    a = a * 16807 % 2147483647;
    b = b * 48271 % 2147483647;
    if ((a & 0xffff) == (b & 0xffff))
    {
      res++;
    }
  }
  return res;
}

uint32_t part2(uint64_t a, uint64_t b)
{
  uint32_t res = 0;
  for (int i = 0; i < 5000000; i++)
  {
    do
    {
      a = a * 16807 % 2147483647;
    } while (a % 4 != 0);

    do
    {
      b = b * 48271 % 2147483647;
    } while (b % 8 != 0);

    if ((a & 0xffff) == (b & 0xffff))
    {
      res += 1;
    }
  }
  return res;
}

int main()
{
  uint64_t a = 873;
  uint64_t b = 583;

  uint32_t p1 = part1(a, b);
  uint32_t p2 = part2(a, b);

  std::cout << "P1: " << p1 << std::endl;
  std::cout << "P2: " << p2 << std::endl;

  return 0;
}
