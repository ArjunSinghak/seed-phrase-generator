#ifndef ENTROPY_HPP
#define ENTROPY_HPP

#include <cstdint>
#include <vector>

namespace seed {

std::vector<uint8_t> generate_entropy(size_t bytes = 16);

} // namespace seed

#endif // ENTROPY_HPP