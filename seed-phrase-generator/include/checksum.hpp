#ifndef CHECKSUM_HPP
#define CHECKSUM_HPP

#include <cstdint>
#include <vector>

namespace seed {

uint8_t compute_checksum(const std::vector<uint8_t>& data);

} // namespace seed

#endif // CHECKSUM_HPP