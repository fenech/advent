require 'digest'

class Enumerator::Lazy
  def filter_map
    Lazy.new(self) do |yielder, *values|
      result = yield *values
      yielder << result if result
    end
  end
end

answer = (1..Float::INFINITY).lazy.filter_map { |i|
  input = "iwrupvqb" + i.to_s
  md5 = Digest::MD5.new
  md5 << input
  hex = md5.hexdigest.to_s
  i if hex.start_with? "00000"
}.first(1)

puts answer
